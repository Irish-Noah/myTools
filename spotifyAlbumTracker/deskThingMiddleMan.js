const http = require('http');
const url = require('url');

const server = http.createServer((req, res) => {
  const parsed = url.parse(req.url, true);

  if (parsed.pathname === '/callback') {
    const params = new URLSearchParams(parsed.query);
    const deskthing = `deskthing://a?app=spotify&${params.toString()}`;

    // Serve an HTML page that redirects via JS instead of a 302
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(`
      <html>
        <body>
          <p>Authenticating with DeskThing...</p>
          <script>
            window.location.href = "${deskthing}";
          </script>
          <noscript>
            <a href="${deskthing}">Click here if not redirected automatically</a>
          </noscript>
        </body>
      </html>
    `);
  } else {
    res.writeHead(404);
    res.end();
  }
});

server.listen(3000, '127.0.0.1', () => {
  console.log('OAuth relay running at http://127.0.0.1:3000');
});