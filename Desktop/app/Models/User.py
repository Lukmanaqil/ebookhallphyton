from collections import OrderedDict
namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Contracts\Auth\MustVerifyEmail;
use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Notifications\Notifiable;
class User (Authenticatable) :
    use Notifiable;
    fillable = OrderedDict([(0,'name'),(1,'email'),(2,'password')]);
    hidden = OrderedDict([(0,'password'),(1,'remember_token')]);
    table = 'userlogin';
    casts = OrderedDict([('email_verified_at','datetime')]);