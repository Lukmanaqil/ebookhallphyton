from collections import OrderedDict

# Manage core logic by this class
class Settlement :
    @staticmethod
    def default_key(d):
        result = 0
        for key, _ in d.items():
           	# Check key is integer and key is not less than result
            if(type(key) is int and key >= result) :
                # Get new key
                result = key + 1
        return result
    
    @staticmethod
    def array_push(target,values):
        # Add new value into collection
        for value in values:
            # add key value
            target[Settlement.default_key(target)] = value   	
            
        return len(target)
    
#---------------------------------
# kalkicode.com 
# These methods have not been changed by our tools.
# session
# view
#----------------------------

namespace App\Http\Controllers;

use App\Models\UserLibrary;
use App\Models\Book;
class userLibraryController (Controller) :
    def view(this) :
        user = UserLibrary.where('email', session('email')).get();
        #$books = Book::where('isbn', $user->isbn)->get();
        books = OrderedDict([]);
        for value in user.values() : 
            Settlement.array_push(books,[Book.where('isbn', value.isbn).first()]);
        
        return view('UserLibrary', OrderedDict([('books',books)]));
    
