from collections import OrderedDict
#---------------------------------
# kalkicode.com 
# These methods have not been changed by our tools.
# view
# session
# request
#----------------------------

namespace App\Http\Controllers;

use App\Models\Book;
use App\Models\UserLibrary;
class MasterLibraryController (Controller) :
    def index(this) :
        books = Book.all();
        return view('MasterLibrary', OrderedDict([('books',books)]));
    
    def addtoUserLibrary(this) :
        books = Book.all();
        book =  UserLibrary();
        book.timestamps = False;
        book.email = session('email');
        book.isbn = request('isbn');
        book.save();
        return view('MasterLibrary', OrderedDict([('books',books)]));
    
