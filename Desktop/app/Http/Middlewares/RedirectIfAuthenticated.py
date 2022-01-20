from collections import OrderedDict
#---------------------------------
# kalkicode.com 
# These methods have not been changed by our tools.
# redirect
# next
#----------------------------

namespace App\Http\Middleware;

use App\Providers\RouteServiceProvider;
use Closure;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
class RedirectIfAuthenticated :
    #*
        # * Handle an incoming request.
        # *
        # * @param  \Illuminate\Http\Request  $request
        # * @param  \Closure  $next
        # * @param  string|null  ...$guards
        # * @return mixed
        # 
        
    def handle(this,Request request, Closure next, ...guards) :
        guards =  OrderedDict([(0,None)]) if empty(guards) else guards;
        for guard in guards.values() : 
            if (Auth.guard(guard).check()) :
                return redirect(RouteServiceProvider().HOME);
            
        
        return next(request);
    
