@extends('layouts.layouts')

@section('content')
<div class="register-photo" style="background-color: rgb(168, 208, 230);">
	<div class="form-container">
		<div class="image-holder" style="background-image: url(&quot;miscImages/library-wallpaper-20.jpg&quot;);"></div>
		<form method="POST" action="{{ route('register') }}">
			@csrf
			<h2 class="text-center">
				<strong>Create</strong> an account.
			</h2>
			<div class="form-group">
				<input id="name" type="text" placeholder="Name" class="form-control @error('name') is-invalid @enderror" name="name" value="{{ old('name') }}" required autocomplete="name" autofocus>

				@error('name')
				<span class="invalid-feedback" role="alert">
					<strong>{{ $message }}</strong>
				</span>
				@enderror
			</div>
			<div class="form-group">
				<input id="email" type="email" placeholder="Email" class="form-control @error('email') is-invalid @enderror" name="email" value="{{ old('email') }}" required autocomplete="email">

				@error('email')
				<span class="invalid-feedback" role="alert">
					<strong>{{ $message }}</strong>
				</span>
				@enderror
			</div>
			<div class="form-group">
				<input id="password" type="password" placeholder="Password" class="form-control @error('password') is-invalid @enderror" name="password" required autocomplete="new-password">

				@error('password')
				<span class="invalid-feedback" role="alert">
					<strong>{{ $message }}</strong>
				</span>
				@enderror
			</div>
			<div class="form-group">
				<input id="password-confirm" type="password" placeholder="Password (repeat)" class="form-control" name="password_confirmation" required autocomplete="new-password">
			</div>
			<div class="form-group"></div>
			<div class="form-group">
				<button class="btn btn-primary btn-block" type="submit" style="background-color: rgb(36, 48, 94);">Sign Up</button>
			</div>
			<a href="/login" class="already">You already have an
				account? Login here.</a>
		</form>
	</div>
</div>
@endsection