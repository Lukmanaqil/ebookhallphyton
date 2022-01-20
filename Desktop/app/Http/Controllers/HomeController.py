#---------------------------------
# kalkicode.com 
# These methods have not been changed by our tools.
# view
#----------------------------

namespace App\Http\Controllers;

use Illuminate\Http\Request;
class HomeController (Controller) :
    #*
        # * Create a new controller instance.
        # *
        # * @return void
        # 
        
    def __init__(this) :
        this.middleware('auth');
    
    #*
        # * Show the application dashboard.
        # *
        # * @return \Illuminate\Contracts\Support\Renderable
        # 
        
    def index(this) :
        return view('home');
    
