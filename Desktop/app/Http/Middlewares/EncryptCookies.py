from collections import OrderedDict
namespace App\Http\Middleware;

use Illuminate\Cookie\Middleware\EncryptCookies as Middleware;
class EncryptCookies (Middleware) :
    #*
        # * The names of the cookies that should not be encrypted.
        # *
        # * @var array
        # 
        
    except = OrderedDict([]);
