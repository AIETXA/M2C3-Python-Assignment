require 'redis'
require 'sinatra'
require 'nanoid'

redis = Redis.new(host: "127.0.0.1", port: 6379)


get '/' do
  <<~HTML
    <!DOCTYPE html>
    <html>
      <head><title>Acortador URL</title></head>
      <body style='font-family: sans-serif; text-align: center; margin-top: 50px;'>   
        <h2>Acortador de enlaces con Redis</h2>
        <form action='/acortar' method='POST'>
          <input type='url' name='url' placeholder='Pega tu URL larga en este lugar' required style='width: 300px; padding: 8px;'>
          <button type='submit' style='padding: 8px 12px;'>Acortar</button>
        </form>
      </body>
    </html>
  HTML
end



post '/acortar' do
    url_original = params[:url]

    codigo = Nanoid.generate(size:6)

    redis.set('url:#{codigo}', url_original)

    url_corta = '#{request.base_url}/#{codigo}'
    "Enlace acortado con éxito: <a href='#{url_corta}'>#{url_corta}</a>"
end    


get '/:codigo' do
    codigo = params[:codigo]

    url_original = redis.get('url:#{codigo}')

    if url_original
        redirect url_original, 302
    else  
        'Error 404: El enlace acortado no existe'
    end
end        
        
