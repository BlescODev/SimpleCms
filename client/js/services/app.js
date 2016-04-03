var app = angular.module('simpleCmsApp', ['ngRoute', 'ngSanitize', 'ngAnimate', 'satellizer']);

app.config(['$routeProvider', '$authProvider', function($routeProvider, $authProvider) {

	$authProvider.loginUrl = "/auth";
	$authProvider.tokenName = "access_token";
	$authProvider.authToken = "JWT";

	$routeProvider
		.when('/login', {
			controller: 'loginCtrl',
			templateUrl: 'html/views/login.tpl.html'
		})
		.when('/404', {
			templateUrl: 'html/views/404.tpl.html'
		})
		.when('/edit', {
			controller: 'editPageCtrl',
			templateUrl: 'html/views/edit-content.tpl.html',
		})
		.when('/edit/:page*', {
			controller: 'editPageCtrl',
			templateUrl: 'html/views/edit-content.tpl.html',
		})
		.when('/setting', {
			controller: 'settingsCtrl',
			templateUrl: 'html/views/settings.tpl.html'
		})
		.when('/settings/:setting*', {
			controller: 'settingsCtrl',
			templateUrl: function(urlattr){
				return 'html/views/' + urlattr.setting + 'Settings.tpl.html';
			},
		})
		.when('/', {
			controller: 'contentCtrl',
			templateUrl: 'html/views/content.tpl.html'
		})
		.when('/:page*', {
			controller: 'contentCtrl',
			templateUrl: 'html/views/content.tpl.html'
		})
		.otherwise({
			templateUrl: 'html/views/404.tpl.html'
		});
}]);

app.service('appService', ['$q', '$location', '$http', '$timeout', 'notificationService', function($q, $location, $http,
	$timeout, notificationService) {

	var properties = [];
	properties["location"] = "http://" + $location.host() + ":" + $location.port() + "/";
	properties["main"] = "/index.scms";
	properties["navigation"] = "/navigation.scms";

	var httpRequest = function(method, url, data, success, error) {

		var params = {};

		if (method === "GET") {
			params = data;
		}

		$http({
				method: method,
				url: url,
				headers: {
					'Content-type': 'application/json'
				},
				data: data,
				params: params
			})
			.then(function(response) {
				if (typeof success === 'function') {
					success(response);
				}
			}, function(response) {
				if (typeof error === 'function') {
					error(response);
				}
			});

	};

	return {
		ready: function(callback) {
			if (typeof callback === 'function') {
				angular.element(document).ready(callback);
			}
		},
		get: function(property) {
			return properties[property];
		},
		http: function(method, url, data, success, error) {
			httpRequest(method, url, data, success, error);
		},
		$location: $location,
		$timeout: $timeout,
		notifications: notificationService
	}
}]);


/*

resolve: {
	auth: function($q, $location, user) {

		var loggedIn = $q.defer();

		if (user.isLoggedIn()) {
			loggedIn.resolve();
		} else {
			loggedIn.reject();
			$location.url("/login");
		}

		return loggedIn.promise;
	}
}

*/
