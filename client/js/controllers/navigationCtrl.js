app.controller('navigationCtrl', ['appService', '$scope', 'pageService', 'user', function(appService, $scope,
	pageService, user) {

	$scope.scrolled = false;

	$scope.inNav = [];
	$scope.outNav = [];

	var inNav = [{
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

	var outNav = [{
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
			$scope.inNav = response.data.content.concat(inNav);
			$scope.outNav = response.data.content.concat(outNav); 
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
