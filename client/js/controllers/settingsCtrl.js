app.controller('settingsCtrl', ['appService', 'settingsService', '$scope', '$routeParams', function(appService, settingsService, $scope, $routeParams) {
	var init = function() {
		settingsService.get($routeParams.setting).then(function(response) {
			$scope.settings = response.data;
			console.log($scope.settings);
		}, function(response) {
			if (response.status == 404) {
				appService.$location.url('/404');
			} else if (response.status == 500) {
				appService.notifications.queue({
					message: "The server is experiencing some problems at the moment. Sorry!",
					type: "error"
				});
			}
		});
	};
	$scope.save = function() {
		setting = {
			'name': $routeParams.setting,
			'settings' : $scope.settings
		}
		settingsService.update(setting).then(function(response) {
			appService.notifications.queue({
				message: "The settings were updated.",
				type: "success"
			});
		}, function(response) {
			$scope.errors = response.data;
			appService.notifications.queue({
				message: "The server is experiencing some problems at the moment. Sorry!",
				type: "error"
			});
		});
	};

	appService.ready(init);
}]);
