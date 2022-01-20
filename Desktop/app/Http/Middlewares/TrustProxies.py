namespace App\Http\Middleware;

use Fideloper\Proxy\TrustProxies as Middleware;
use Illuminate\Http\Request;
class TrustProxies (Middleware) :
    #*
        # * The trusted proxies for this application.
        # *
        # * @var array|string|null
        # 
        
    proxies = None;
    #*
        # * The headers that should be used to detect proxies.
        # *
        # * @var int
        # 
        
    headers = Request().HEADER_X_FORWARDED_FOR | Request().HEADER_X_FORWARDED_HOST | Request().HEADER_X_FORWARDED_PORT | Request().HEADER_X_FORWARDED_PROTO | Request().HEADER_X_FORWARDED_AWS_ELB;
