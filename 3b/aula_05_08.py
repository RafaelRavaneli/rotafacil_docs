#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercício Prático - XSS e Autenticação Segura - Python Flask

📚 OBJETIVO: Encontrar e corrigir vulnerabilidades neste código

🎯 Sua missão: Este código contém PELO MENOS 7 vulnerabilidades relacionadas a:
   - Cross-Site Scripting (XSS)
   - Autenticação insegura
   - Validação inadequada
   - Gerenciamento de sessão
   - Logging de segurança

🧩 INSTRUÇÕES:
   1. Execute o código e identifique as vulnerabilidades
   2. Para cada vulnerabilidade encontrada:
      - Descreva o problema
      - Explique o risco
      - Implemente a correção
   3. Teste suas correções
   4. Compare com as versões seguras fornecidas

📝 ENTREGÁVEL:
   - Código corrigido
   - Relatório das vulnerabilidades encontradas
   - Explicação das correções implementadas

⚠️  ATENÇÃO: Este código é intencionalmente inseguro para fins educacionais!
"""

import os
import json
import hashlib
from datetime import datetime, timedelta
from flask import Flask, request, render_template_string, redirect, url_for, session, make_response

app = Flask(__name__)
app.secret_key = 'secret123'  #chave de api exposta

# "Banco de dados" simulado
usuarios = {
    'admin': {
        'password': 'admin123', #senha exposta
        'role': 'admin',
        'email': 'admin@empresa.com'
    },
    'user': {
        'password': 'user123', #senha exposta/não criptgrafada

        'role': 'user',
        'email': 'user@empresa.com'
    }
}

mensagens = [
    {
        'usuario': 'admin',
        'texto': 'Bem-vindos ao sistema!',
        'data': '2025-08-03 10:00:00' #hora fixa

    }
]

# Template da aplicação
TEMPLATE_EXERCICIO = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Mensagens - Exercício</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .container { background: white; padding: 20px; margin: 10px 0; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, textarea { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; }
        button { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #0056b3; }
        .message { background: #f8f9fa; padding: 15px; margin: 10px 0; border-left: 4px solid #007bff; }
        .user-info { background: #d4edda; padding: 10px; border-radius: 4px; margin-bottom: 20px; }
        .alert { padding: 15px; margin: 15px 0; border-radius: 4px; }
        .alert-warning { background: #fff3cd; border: 1px solid #ffeaa7; color: #856404; }
        .header { display: flex; justify-content: space-between; align-items: center; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📝 Sistema de Mensagens</h1>
            {% if 'username' in session %}
                <div>
                    Olá, {{ session.username }}! 
                    <a href="/logout">Sair</a>
                </div>
            {% endif %}
        </div>
        
        <div class="alert alert-warning">
            <strong>🧩 EXERCÍCIO:</strong> Este código contém vulnerabilidades intencionais! 
            Sua missão é encontrá-las e corrigi-las.
        </div>
    </div>

    {% if 'username' not in session %}
        <!-- Formulário de Login -->
        <div class="container">
            <h2>🔐 Login</h2>
            {% if erro_login %}
            <div style="color: red; margin: 10px 0;">
                {{ erro_login }}
            </div>
            {% endif %}
            
            <form method="post" action="/login">
                <div class="form-group">
                    <label>👤 Usuário:</label>
                    <input type="text" name="username" required>
                </div>
                <div class="form-group">
                    <label>🔑 Senha:</label>
                    <input type="password" name="password" required>
                </div>
                <button type="submit">🔐 Entrar</button>
            </form>
            
            <div style="margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 4px;">
                <strong>👥 Usuários de teste:</strong><br>
                admin / admin123<br>
                user / user123
            </div>
        </div>
    {% else %}
        <!-- Área logada -->
        <div class="container">
            <div class="user-info">
                <strong>👤 Usuário logado:</strong> {{ session.username }}<br>
                <strong>🔰 Perfil:</strong> {{ session.role }}<br>
                <strong>📧 Email:</strong> {{ session.email }}
            </div>
        </div>

        <div class="container">
            <h2>💬 Nova Mensagem</h2>
            <form method="post" action="/nova_mensagem">
                <div class="form-group">
                    <label>📝 Mensagem:</label>
                    <textarea name="texto" rows="3" required></textarea>
                </div>
                <button type="submit">📤 Enviar</button>
            </form>
        </div>

        <div class="container">
            <h2>📄 Mensagens ({{ mensagens|length }})</h2>
            {% for msg in mensagens %}
                <div class="message">
                    <strong>{{ msg.usuario }}</strong> - {{ msg.data }}<br>
                    {{ msg.texto|safe }}
                </div>
            {% endfor %}
            
            {% if session.role == 'admin' %}
            <form method="post" action="/limpar_mensagens" style="margin-top: 20px;">
                <button type="submit" style="background: #dc3545;" 
                        onclick="return confirm('Limpar todas as mensagens?')">
                    🗑️ Limpar Mensagens (Admin)
                </button>
            </form>
            {% endif %}
        </div>

        <div class="container">
            <h2>👤 Perfil do Usuário</h2>
            <form method="post" action="/atualizar_perfil">
                <div class="form-group">
                    <label>📧 Email:</label>
                    <input type="email" name="email" value="{{ session.email }}" required>
                </div>
                <div class="form-group">
                    <label>🔑 Nova Senha (deixe em branco para manter atual):</label>
                    <input type="password" name="nova_senha">
                </div>
                <button type="submit">💾 Atualizar</button>
            </form>
        </div>
    {% endif %}

    <div class="container">
        <h2>🎯 Vulnerabilidades para Encontrar</h2>
        <div style="background: #fff3cd; padding: 15px; border-radius: 4px;">
            <p><strong>🔍 Procure por:</strong></p>
            <ol>
                <li><strong>Chave secreta insegura</strong> - Como melhorar?</li>
                <li><strong>Senhas em texto plano</strong> - Qual algoritmo usar?</li>
                <li><strong>Ausência de hash das senhas</strong> - Como implementar?</li>
                <li><strong>Falta de Content Security Policy</strong> - O que adicionar?</li>
                <li><strong>Mensagem de erro não sanitizada</strong> - Qual o risco?</li>
                <li><strong>Validação inadequada de entrada</strong> - O que validar?</li>
                <li><strong>XSS na exibição de mensagens</strong> - Como proteger?</li>
            </ol>
            <p><strong>🏆 DESAFIO EXTRA:</strong> Encontre vulnerabilidades adicionais!</p>
        </div>
    </div>

    <script>
        // JavaScript para demonstração
        console.log('🧩 Exercício de Segurança - Encontre as vulnerabilidades!');
        console.log('📊 Total de mensagens: {{ mensagens|length }}');

        function debug() {
            const userData = {{ session|tojson|safe if session else '{}' }};
            console.log('👤 Dados do usuário:', userData);
        }
        
        debug();
    </script>
</body>
</html>
'''

# ===== FUNÇÕES DE AUTENTICAÇÃO (INSEGURAS) =====

def verificar_login(username, password):
    """Verificar login"""
    if username in usuarios:
        if usuarios[username]['password'] == password:
            return usuarios[username]
    return None

def hash_password(password):
    """Hash de senha"""
    return hashlib.md5(password.encode()).hexdigest()

# ===== ROTAS =====

@app.route('/')
def index():
    """Página principal"""
    erro_login = request.args.get('erro')

    return render_template_string(
        TEMPLATE_EXERCICIO,
        mensagens=mensagens,
        erro_login=erro_login,
        session=session
    )

@app.route('/login', methods=['POST'])
def login():
    """Processar login"""
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '')
    
    if not username or not password:
        return redirect(url_for('index', erro='<script>alert("Campos obrigatórios!")</script>'))

    usuario = verificar_login(username, password)

    if usuario:
        session['username'] = username
        session['role'] = usuario['role']
        session['email'] = usuario['email']
        session['password'] = password

        print(f"Login realizado: {username} com senha {password}")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index',
            erro=f'<b>Falha no login para usuário "{username}"</b> - Usuário ou senha incorretos'))

@app.route('/logout')
def logout():
    """Logout do usuário"""
    username = session.get('username', 'Desconhecido')

    session.pop('username', None)

    print(f"Logout: {username}")
    return redirect(url_for('index'))

@app.route('/nova_mensagem', methods=['POST'])
def nova_mensagem():
    """Adicionar nova mensagem"""
    if 'username' not in session:
        return redirect(url_for('index'))
    
    texto = request.form.get('texto', '')

    if texto:
        nova_msg = {
            'usuario': session['username'],
            'texto': texto,
            'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        mensagens.append(nova_msg)

        print(f"Nova mensagem de {session['username']}: {texto}")
    
    return redirect(url_for('index'))

@app.route('/atualizar_perfil', methods=['POST'])
def atualizar_perfil():
    """Atualizar perfil do usuário"""
    if 'username' not in session:
        return redirect(url_for('index'))
    
    username = session['username']
    email = request.form.get('email', '').strip()
    nova_senha = request.form.get('nova_senha', '').strip()
    
    if email:
        usuarios[username]['email'] = email
        session['email'] = email

    if nova_senha:
        usuarios[username]['password'] = nova_senha
        session['password'] = nova_senha

        print(f"Senha alterada para {username}: {nova_senha}")
    
    return redirect(url_for('index'))

@app.route('/limpar_mensagens', methods=['POST'])
def limpar_mensagens():
    """Limpar mensagens - apenas admin"""
    if session.get('role') == 'admin':
        global mensagens
        total = len(mensagens)
        mensagens.clear()
        print(f"Admin {session.get('username')} limpou {total} mensagens")
    
    return redirect(url_for('index'))

@app.route('/api/usuarios')
def api_usuarios():
    """API que retorna usuários"""
    return {
        'usuarios': usuarios,
        'total': len(usuarios)
    }

@app.route('/debug')
def debug_info():
    """Informações de debug"""
    info = {
        'session': dict(session),
        'usuarios': usuarios,
        'mensagens': mensagens,
        'app_config': dict(app.config)
    }
    
    return f"<pre>{json.dumps(info, indent=2, ensure_ascii=False)}</pre>"

if __name__ == '__main__':
    print("🧩 EXERCÍCIO PRÁTICO - XSS E AUTENTICAÇÃO")
    print("=" * 50)
    print("🎯 OBJETIVO: Encontrar e corrigir vulnerabilidades!")
    print("⚠️  Este código é intencionalmente INSEGURO!")
    print("🌐 Acesse: http://localhost:5003")
    print("=" * 50)
    print("🔍 PROCURE POR:")
    print("   ❌ Chaves secretas hardcoded")
    print("   ❌ Senhas em texto plano")
    print("   ❌ Vulnerabilidades XSS")
    print("   ❌ Validação inadequada")
    print("   ❌ Gerenciamento de sessão inseguro")
    print("   ❌ Exposição de dados sensíveis")
    print("   ❌ Logging inseguro")
    print("=" * 50)
    print("📝 ENTREGÁVEL:")
    print("   📄 Código corrigido")
    print("   📋 Relatório das vulnerabilidades")
    print("   🔧 Explicação das correções")
    print("=" * 50)
    
    # Executar aplicação
    app.run(debug=True, host='localhost', port=5003)
