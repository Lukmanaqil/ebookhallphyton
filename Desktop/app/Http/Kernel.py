from collections import OrderedDict
namespace App\Http;

use Illuminate\Foundation\Http\Kernel as HttpKernel;
class Kernel (HttpKernel) :
    #*
        # * The application's global HTTP middleware stack.
        # *
        # * These middleware are run during every request to your application.
        # *
        # * @var array
        # 
        
    middleware = OrderedDict([(0,\App\Http\Middleware\TrustProxies().class),(1,\Fruitcake\Cors\HandleCors().class),(2,\App\Http\Middleware\PreventRequestsDuringMaintenance().class),(3,\Illuminate\Foundation\Http\Middleware\ValidatePostSize().class),(4,\App\Http\Middleware\TrimStrings().class),(5,\Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull().class)]);
    #*
        # * The application's route middleware groups.
        # *
        # * @var array
        # 
        
    middlewareGroups = OrderedDict([('web',OrderedDict([(0,\App\Http\Middleware\EncryptCookies().class),(1,\Illuminate\Cookie\Middleware\AddQueuedCookiesToResponse().class),(2,\Illuminate\Session\Middleware\StartSession().class),(3,\Illuminate\View\Middleware\ShareErrorsFromSession().class),(4,\App\Http\Middleware\VerifyCsrfToken().class),(5,\Illuminate\Routing\Middleware\SubstituteBindings().class),(6,\RenatoMarinho\LaravelPageSpeed\Middleware\ElideAttributes().class),(7,\RenatoMarinho\LaravelPageSpeed\Middleware\InsertDNSPrefetch().class),(8,\RenatoMarinho\LaravelPageSpeed\Middleware\RemoveComments().class),(9,\RenatoMarinho\LaravelPageSpeed\Middleware\CollapseWhitespace().class),(10,\RenatoMarinho\LaravelPageSpeed\Middleware\DeferJavascript().class)])),('api',OrderedDict([(0,'throttle:api'),(1,\Illuminate\Routing\Middleware\SubstituteBindings().class)]))]);
    #*
        # * The application's route middleware.
        # *
        # * These middleware may be assigned to groups or used individually.
        # *
        # * @var array
        # 
        
    routeMiddleware = OrderedDict([('auth',\App\Http\Middleware\Authenticate().class),('auth.basic',\Illuminate\Auth\Middleware\AuthenticateWithBasicAuth().class),('cache.headers',\Illuminate\Http\Middleware\SetCacheHeaders().class),('can',\Illuminate\Auth\Middleware\Authorize().class),('guest',\App\Http\Middleware\RedirectIfAuthenticated().class),('password.confirm',\Illuminate\Auth\Middleware\RequirePassword().class),('signed',\Illuminate\Routing\Middleware\ValidateSignature().class),('throttle',\Illuminate\Routing\Middleware\ThrottleRequests().class),('verified',\Illuminate\Auth\Middleware\EnsureEmailIsVerified().class)]);
