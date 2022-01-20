from collections import OrderedDict
namespace App\Http\Controllers\Auth;

use App\Http\Controllers\Controller;
use App\Providers\RouteServiceProvider;
use App\Models\User;
use Illuminate\Foundation\Auth\RegistersUsers;
use Illuminate\Support\Facades\Hash;
use Illuminate\Support\Facades\Validator;
class RegisterController (Controller) :
    #
        #|--------------------------------------------------------------------------
        #| Register Controller
        #|--------------------------------------------------------------------------
        #|
        #| This controller handles the registration of new users as well as their
        #| validation and creation. By default this controller uses a trait to
        #| provide this functionality without requiring any additional code.
        #|
        #
        
    use RegistersUsers;
    #*
        # * Where to redirect users after registration.
        # *
        # * @var string
        # 
        
    redirectTo = RouteServiceProvider().LOGIN;
    #*
        # * Create a new controller instance.
        # *
        # * @return void
        # 
        
    def __init__(this) :
        this.middleware('guest');
    
    #*
        # * Get a validator for an incoming registration request.
        # *
        # * @param  array  $data
        # * @return \Illuminate\Contracts\Validation\Validator
        # 
        
    def validator(this,array data) :
        return Validator.make(data, OrderedDict([('name',OrderedDict([(0,'required'),(1,'string'),(2,'max:255')])),('email',OrderedDict([(0,'required'),(1,'string'),(2,'email'),(3,'max:255'),(4,'unique:users')])),('password',OrderedDict([(0,'required'),(1,'string'),(2,'min:8'),(3,'confirmed')]))]));
    
    #*
        # * Create a new user instance after a valid registration.
        # *
        # * @param  array  $data
        # * @return \App\Models\User
        # 
        
    def create(this,array data) :
        return User.create(OrderedDict([('name',data['name']),('email',data['email']),('password',Hash.make(data['password']))]));
    
