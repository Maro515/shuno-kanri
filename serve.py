"""ローカル検証用サーバー。キャッシュを無効化して常に最新ファイルを返す。
   （教材フォルダは100以上のファイルを読むためスレッド対応にしている）"""
import sys, http.server, socketserver

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        super().end_headers()
    def log_message(self, *a):
        pass

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8861
socketserver.ThreadingTCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(('', port), NoCacheHandler) as httpd:
    print(f'serving on http://localhost:{port} (no-cache)')
    httpd.serve_forever()
