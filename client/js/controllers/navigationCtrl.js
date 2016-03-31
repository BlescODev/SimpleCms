app.controller('navigationCtrl', ['appService', '$scope', 'pageService', 'user', function(appService, $scope,
	pageService, user) {

	$scope.scrolled = false;

	$scope.nav = [];

	$scope.inNav = [{
			"title": "SimpleCms",
			"url": "",
			"children": [{
				"title": "Edit",
				"url": "#/edit/{{current.page}}"
			},{
				"title": "Logout",
				"url": ""
			}]
		}];

	$scope.outNav = [{
			"title": "SimpleCms",
			"url": "",
			"children": [{
				"title": "Login",
				"url": "#/login"
			}]
		}];



	var init = function() {
		navigation = appService.get('navigation').substr(1)
		pageService.get(navigation).then(function(response) {
			$scope.nav = response.data.content; 
		}, function(response) {
			appService.notifications.queue({
				message: "Unable to retrieve navigation data!",
				type: "error"
			});
		});
	};

	appService.ready(init);

	window.addEventListener('scroll', function(e) {
		$scope.scrolled = window.pageYOffset != 0;
		$scope.$apply();
	});

	$scope.isAuthenticated = function() {
		return user.isLoggedIn();
	};

	$scope.logout = function() {
		user.logout();
		appService.$location.url("/login")
	};
}]);

/*

<li>
<a>SimpleCms</a>
<ul>
<li ng-if="isAuthenticated()">
<a href="#/edit{{route}}">Edit this Page</a>
</li>
<li ng-if="isAuthenticated()">
<a href="/pages/">Pages</a>
</li>
<li ng-if="isAuthenticated()">
<a href="#/settings">Settings</a>
</li>
<li ng-if="!isAuthenticated()">
<a href="#/login">Login</a>
</li>
<li ng-if="isAuthenticated()">
<a ng-click="logout()">Logout</a>
</li>
</ul>
</li>

*/
