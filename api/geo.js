// Returns the visitor's country (Vercel geo header) so js/analytics.js knows whether to show the
// cookie banner (EEA, UK, Switzerland). Tiny, no dependencies, private short cache. No override parameter.
export const config = { runtime: 'edge' };

export default function handler(request) {
  const country = (request.headers.get('x-vercel-ip-country') || '').toUpperCase().slice(0, 2);
  return new Response(JSON.stringify({ country }), {
    headers: {
      'content-type': 'application/json; charset=utf-8',
      'cache-control': 'private, max-age=300',
      'vary': 'x-vercel-ip-country'
    }
  });
}
