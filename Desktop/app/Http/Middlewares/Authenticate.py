#---------------------------------
# kalkicode.com 
# These methods have not been changed by our tools.
# route
#----------------------------

namespace App\Http\Middleware;

use Illuminate\Auth\Middleware\Authenticate as Middleware;
class Authenticate (Middleware) :
    #*
        # * Get the path the user should be redirected to when they are not authenticated.
        # *
        # * @param  \Illuminate\Http\Request  $request
        # * @return string|null
        # 
        
    def redirectTo(this,request) :
        if (not request.expectsJson()) :
            return route('login');
        
    
