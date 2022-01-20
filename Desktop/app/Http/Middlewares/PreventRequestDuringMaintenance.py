from collections import OrderedDict
namespace App\Http\Middleware;

use Illuminate\Foundation\Http\Middleware\PreventRequestsDuringMaintenance as Middleware;
class PreventRequestsDuringMaintenance (Middleware) :
    #*
        # * The URIs that should be reachable while maintenance mode is enabled.
        # *
        # * @var array
        # 
        
    except = OrderedDict([]);
