from collections import OrderedDict
namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\TrimStrings as Middleware;
class TrimStrings (Middleware) :
    #*
        # * The names of the attributes that should not be trimmed.
        # *
        # * @var array
        # 
        
    except = OrderedDict([(0,'current_password'),(1,'password'),(2,'password_confirmation')]);
