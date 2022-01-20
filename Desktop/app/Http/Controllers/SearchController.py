from collections import OrderedDict
#---------------------------------
# kalkicode.com 
# These methods have not been changed by our tools.
# request
# view
#----------------------------

namespace App\Http\Controllers;

use App\Models\Book;
class SearchController (Controller) :
    def search(this) :
        value = request('Search');
        type = request('bookCheck');
        if (type == 'ISBN') :
            books = Book.where('isbn', value).get();
            return view('MasterLibrary', OrderedDict([('books',books)]));
        else : 
            if (type == 'Genre') :
                books = Book.where('genre', value).get();
                return view('MasterLibrary', OrderedDict([('books',books)]));
            else : 
                if (type == 'Title') :
                    books = Book.where('title', value).get();
                    return view('MasterLibrary', OrderedDict([('books',books)]));
                
            
        
    
