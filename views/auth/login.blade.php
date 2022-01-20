@extends('layouts.layouts')

@section('content')
<div class="login-clean" style="background-color: rgb(168, 208, 230);">
    <form method="post" action="{{ route('login') }}">
        @csrf
        <h2 class="sr-only">Login Form</h2>
        <img src="miscImages/istockphoto-863958484-612x612.jpg" style="width: 150px; margin: 0; margin-right: 99px; margin-left: 50px; margin-bottom: 0px; height: 150px;">
        <div class="form-group">
            <input id="email" type="email" placeholder="Email" class="form-control @error('email') is-invalid @enderror" name="email" value="{{ old('email') }}" required autocomplete="email" autofocus>

            @error('email')
            <span class="invalid-feedback" role="alert">
                <strong>{{ $message }}</strong>
            </span>
            @enderror
        </div>
        <div class="form-group">
            <input id="password" type="password" placeholder="Password" class="form-control @error('password') is-invalid @enderror" name="password" required autocomplete="current-password">

            @error('password')
            <span class="invalid-feedback" role="alert">
                <strong>{{ $message }}</strong>
            </span>
            @enderror
        </div>
        <div class="form-check">
            <input class="form-check-input" type="checkbox" name="remember" id="remember" {{ old('remember') ? 'checked' : '' }}>

            <label class="form-check-label" for="remember">
                {{ __('Remember Me') }}
            </label>
        </div>
        <div class="form-group">
            <button type="submit" class="btn btn-primary btn-block" style="background-color: rgb(36, 48, 94);">
                {{ __('Login') }}
            </button>
        </div>
        <div class="form-group">
            @if (Route::has('password.request'))
            <a class="forgot" href="{{ route('password.request') }}">
                {{ __('Forgot Your Password?') }}
            </a>
            @endif
        </div>
        <a href="/register" class="forgot">Sign Up</a>
        <p></p>
        @if (session('status'))
        <div class="alert alert-success" style="text-align: center" role="alert">
            {{ session('status') }}
        </div>
        @endif
    </form>
</div>
@endsection