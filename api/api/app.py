from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from urllib.parse import urlparse
import time

app = Flask(__name__)
CORS(app)  # Permite requisições de qualquer origem

@app.route('/')
def home():
    return jsonify({
        'status': 'online',
        'message': 'API de Validação de QR Codes - OneDrive/SharePoint',
        'version': '1.0.0'
    })

@app.route('/validate', methods=['POST'])
def validate_url():
    """
    Valida se uma URL do OneDrive/SharePoint está acessível
    """
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({
                'valid': False,
                'error': 'URL não fornecida'
            }), 400
        
        # Verifica se é realmente um link do OneDrive/SharePoint
        if not is_onedrive_url(url):
            return jsonify({
                'valid': False,
                'error': 'Não é um link do OneDrive/SharePoint'
            })
        
        # Tenta acessar a URL
        is_valid, error_message = check_url_accessibility(url)
        
        return jsonify({
            'valid': is_valid,
            'url': url,
            'error': error_message if not is_valid else None,
            'timestamp': time.time()
        })
    
    except Exception as e:
        return jsonify({
            'valid': False,
            'error': f'Erro interno: {str(e)}'
        }), 500

@app.route('/validate-batch', methods=['POST'])
def validate_batch():
    """
    Valida múltiplas URLs de uma vez
    """
    try:
        data = request.get_json()
        urls = data.get('urls', [])
        
        if not urls or not isinstance(urls, list):
            return jsonify({
                'error': 'Lista de URLs inválida'
            }), 400
        
        results = []
        for url in urls:
            if isinstance(url, dict):
                url_str = url.get('url')
            else:
                url_str = url
            
            is_valid, error_message = check_url_accessibility(url_str)
            results.append({
                'url': url_str,
                'valid': is_valid,
                'error': error_message if not is_valid else None
            })
        
        return jsonify({
            'results': results,
            'total': len(results),
            'valid_count': sum(1 for r in results if r['valid']),
            'error_count': sum(1 for r in results if not r['valid'])
        })
    
    except Exception as e:
        return jsonify({
            'error': f'Erro interno: {str(e)}'
        }), 500

def is_onedrive_url(url):
    """
    Verifica se a URL é do OneDrive ou SharePoint
    """
    try:
        parsed = urlparse(url.lower())
        domain = parsed.netloc
        
        onedrive_domains = [
            'sharepoint.com',
            '1drv.ms',
            'onedrive.live.com',
            'onedrive.com',
            'my.sharepoint.com'
        ]
        
        return any(domain.endswith(d) or d in domain for d in onedrive_domains)
    except:
        return False

def check_url_accessibility(url, timeout=10):
    """
    Verifica se a URL está acessível
    Retorna: (is_valid: bool, error_message: str or None)
    """
    try:
        # Headers para simular um navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        
        # Faz uma requisição HEAD primeiro (mais rápido)
        response = requests.head(url, headers=headers, timeout=timeout, allow_redirects=True)
        
        # Se HEAD não funcionar, tenta GET
        if response.status_code >= 400:
            response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True, stream=True)
            # Lê apenas os primeiros bytes
            next(response.iter_content(chunk_size=1024), None)
        
        # Códigos de sucesso
        if response.status_code in [200, 201, 202, 203, 204, 206, 304]:
            return True, None
        
        # Códigos de redirecionamento considerados OK
        elif response.status_code in [301, 302, 303, 307, 308]:
            return True, None
        
        # Códigos de erro do cliente
        elif response.status_code in [401, 403]:
            return False, f'Acesso negado (HTTP {response.status_code})'
        
        elif response.status_code == 404:
            return False, 'Página não encontrada (HTTP 404)'
        
        elif response.status_code == 410:
            return False, 'Conteúdo removido permanentemente (HTTP 410)'
        
        # Códigos de erro do servidor
        elif response.status_code >= 500:
            return False, f'Erro no servidor (HTTP {response.status_code})'
        
        else:
            return False, f'Status HTTP desconhecido: {response.status_code}'
    
    except requests.exceptions.Timeout:
        return False, 'Tempo de resposta excedido (Timeout)'
    
    except requests.exceptions.SSLError:
        return False, 'Erro de certificado SSL'
    
    except requests.exceptions.ConnectionError:
        return False, 'Erro de conexão - URL inacessível'
    
    except requests.exceptions.TooManyRedirects:
        return False, 'Muitos redirecionamentos'
    
    except requests.exceptions.InvalidURL:
        return False, 'URL inválida'
    
    except Exception as e:
        return False, f'Erro desconhecido: {str(e)}'

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint para verificar se a API está funcionando
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time()
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
