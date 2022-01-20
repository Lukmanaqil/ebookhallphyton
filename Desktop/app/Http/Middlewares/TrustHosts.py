from collections import OrderedDict
namespace App\Http\Middleware;

use Illuminate\Http\Middleware\TrustHosts as Middleware;
class TrustHosts (Middleware) :
    #*
        # * Get the host patterns that should be trusted.
        # *
        # * @return array
        # 
        
    def hosts(this) :
        return OrderedDict([(0,this.allSubdomainsOfApplicationUrl())]);
    
