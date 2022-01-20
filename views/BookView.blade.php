@extends('layouts.secondLayout')

@section('content')
<nav class="navbar navbar-light navbar-expand-lg fixed-top bg-white clean-navbar">
    <div class="container"><a class="navbar-brand logo" href="/book">E-BookHall</a>
    </div>
</nav>
<main class="page product-page">
    <section class="clean-block clean-product dark" style="background-color: #a8d0e6;height: 697px;">
        <div class="container">
            <div class="block-content" style="background-color: #374785;">
                <div class="product-info">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="gallery">
                                <img class="img-fluid d-block mx-auto" src="{{asset($books->coverpage)}}">
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="info" style="margin-top: -500px;margin-left:550px; width:550px; height:550px;">
                                <h3 style="color: #ffffff;">{{$books->title}}</h3>
                                <h3 style="color: rgba(255,255,255,0.5);font-size: 20px;">{{$books->genre}}</h3>
                                <p style="top:-50px;color: rgba(255,255,255)">{{$books->description}}</p>
                                <p style="top:-50px;color: rgba(255,255,255)">Author : {{$books->author}}</p>
                                <p style="top:-50px;color: rgba(255,255,255)">ISBN : {{$books->isbn}}</p>
                                <div class="rating"></div>
                                <div class="price">
                                </div>
                                <input type="hidden" name="isbn" value="{{$books->isbn}}">
                                <button class="btn btn-primary" type="button" onclick="location.href='{{asset($books->bookContents)}}'" style="background-color: #f76c6c;">Read</button>
                                <p>{{ round(microtime(true) - LARAVEL_START, 5) }}</p>
                                <div class="summary">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</main>
<footer class="page-footer dark">
    <div class="container">
        <div class="row">
            <div class="col-sm-3">
                <p style="text-align: center;">Page Load Time = {{ round(microtime(true) - LARAVEL_START, 5) }}ms</p>
            </div>
        </div>
    </div>
</footer>
@endsection