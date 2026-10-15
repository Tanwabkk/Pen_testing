import sqlite3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

# Initialize a local SQLite database with a sample user
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'SuperSecretPassword123')")
    conn.commit()
    conn.close()

init_db()

HTML_PAGE = '''
<!doctype html>
<title>SQL Injection Demo</title>
<h2>{{ title }}</h2>
<form method="POST">
  Username: <input type="text" name="username"><br><br>
  Password: <input type="password" name="password"><br><br>
  <input type="submit" value="Login">
</form>
{% if message %}
  <h3>Result:</h3>
  <p>{{ message }}</p>
{% endif %}
<br><a href="/">Back to Home</a>
'''

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path).path
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        if parsed_path == '/':
            self.wfile.write(b'''
                <h2>SQL Injection Demo App (No Pip Required)</h2>
                <ul>
                    <li><a href="/vulnerable">Vulnerable Login Form</a></li>
                    <li><a href="/secure">Secure Login Form</a></li>
                </ul>
            ''')
        elif parsed_path == '/vulnerable':
            page = HTML_PAGE.replace('{{ title }}', 'Vulnerable Login Form').replace('{% if message %}{% endif %}', '')
            self.wfile.write(page.encode())
        elif parsed_path == '/secure':
            page = HTML_PAGE.replace('{{ title }}', 'Secure Login Form').replace('{% if message %}{% endif %}', '')
            self.wfile.write(page.encode())

    def do_POST(self):
        parsed_path = urlparse(self.path).path
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)
        
        username = params.get('username', [''])[0]
        password = params.get('password', [''])[0]
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        message = ""
        if parsed_path == '/vulnerable':
            # VULNERABLE: Direct string concatenation
            query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
            print(f"Executing Query: {query}")
            try:
                cursor.execute(query)
                user = cursor.fetchone()
                if user:
                    message = f"Login Successful! Welcome, {user[1]}."
                else:
                    message = "Login Failed: Invalid credentials."
            except Exception as e:
                message = f"Database Error: {e}"
                
        elif parsed_path == '/secure':
            # SECURE: Parameterized query
            query = "SELECT * FROM users WHERE username = ? AND password = ?"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            if user:
                message = f"Login Successful! Welcome, {user[1]}."
            else:
                message = "Login Failed: Invalid credentials."
                
        conn.close()
        
        title = 'Vulnerable Login Form' if parsed_path == '/vulnerable' else 'Secure Login Form'
        page = HTML_PAGE.replace('{{ title }}', title)
        page = page.replace('{% if message %}', '').replace('{% endif %}', '')
        page = page.replace('{{ message }}', message)
        
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(page.encode())

if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 8000), SimpleHandler)
    print("Server running at http://127.0.0.1:8000")
    server.serve_forever()
