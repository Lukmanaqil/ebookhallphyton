from collections import OrderedDict
#---------------------------------
# kalkicode.com 
# These methods have not been changed by our tools.
# view
#----------------------------

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Book;
class BookViewController (Controller) :
    def view(this,isbn) :
        book = Book.where('isbn', isbn).first();
        return view('BookView', OrderedDict([('books',book)]));