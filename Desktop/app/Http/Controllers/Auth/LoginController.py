namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use App\Providers\RouteServiceProvider;
use Illuminate\Foundation\Auth\AuthenticatesUsers;
use App\Models\AuditLog;
class LoginController (Controller) :
    #
        #|--------------------------------------------------------------------------
        #| Login Controller
        #|--------------------------------------------------------------------------
        #|
        #| This controller handles authenticating users for the application and
        #| redirecting them to your home screen. The controller uses a trait
        #| to conveniently provide its functionality to your applications.
        #|
        #
        
    use AuthenticatesUsers;
    #*
        # * Where to redirect users after login.
        # *
        # * @var string
        # 
        
    redirectTo = RouteServiceProvider().HOME;
    #*
        # * Create a new controller instance.
        # *
        # * @return void
        # 
        
    def __init__(this) :
        this.middleware('guest').except('logout');
    