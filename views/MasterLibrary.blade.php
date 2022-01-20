@extends('layouts.layouts')

@section('content')
<div style="background-color: rgb(168, 208, 230);">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active"><a class="nav-link" href="/book">Home <span class="sr-only">(current)</span>
                    </a></li>
                <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Account </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="/userlibrary">My Library</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="/">Log out</a>
                    </div>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0" target="_self" action="/book/search">
                <input class="form-control mr-sm-2" type="search" name="Search" placeholder="Browse" aria-label="Search" id="search-field">
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="bookCheck" value="ISBN" id="formCheck-1"><label class="form-check-label" for="formCheck-1" style="color: rgb(0, 0, 0); height: 70px;">ISBN&nbsp;
                        &nbsp;</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="bookCheck" value="Genre" id="formCheck-2"><label class="form-check-label" for="formCheck-2" style="color: rgb(0, 0, 0);">Genre&nbsp; &nbsp;</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="bookCheck" value="Title" id="formCheck-3"><label class="form-check-label" for="formCheck-3" style="color: rgb(0, 0, 0);">Title &nbsp; &nbsp; &nbsp;
                        &nbsp;</label>
                </div>
                <button class="btn btn-outline-primary my-2 my-sm-0" type="submit">Browse</button>
            </form>
        </div>
    </nav>
    <div class="container" style="background-color: transparent;">
        <div class="row justify-content-center">
            <div class="col-xl-10"></div>
            @foreach($books as $book)
            <div class="col-md-6" style="padding: 0; min-width: 480px; margin-top: 10px;">
                <div>
                    <img class="d-block float-left mobile-center" src=" {{asset($book->coverpage)}}" style="width: 220px; height: 276px;">
                </div>
                <br> <strong>TITLE : {{$book->title}}</strong><br> <strong>ISBN : {{$book->isbn}}<br><br><br></strong>
                <form action="/book/{{$book->isbn}}">
                    @csrf
                    <button class="btn btn-primary" type="submit" style="position: relative; top: 14px">View Book</button>
                </form>
                <form action="/book" method="post">
                    @csrf
                    <button style="position: relative; top: -40px; left: 110px" class="btn btn-primary" name="isbn" type="submit" value="{{$book->isbn}}">Add to library</button>
                </form>

            </div>
            @endforeach
            <p style="text-align: center;">Page Load Time = {{ round(microtime(true) - LARAVEL_START, 5) }}s</p>
        </div>
    </div>
</div>
<script src="{{asset('script/jquery.min.js')}}"></script>
<script src="{{asset('script/bootstrap.min.js')}}"></script>
@endsection