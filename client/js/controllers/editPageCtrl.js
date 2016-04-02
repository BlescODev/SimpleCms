app.controller('editPageCtrl', ['appService', 'pageService', '$scope', '$routeParams',
		function(appService, pageService, $scope, $routeParams) {

	var init = function() {
		console.log($routeParams);
		pageService.get($routeParams.page).then(function(response) {
			$scope.page = response.data;
		}, function(response) {
			if (response.status == 500) {
				appService.notifications.queue({
					message: "The server is experiencing some problems at the moment. Sorry!",
					type: "error"
				});
			} else if (response.status == 404) {
				pageService.get("page-templage.scms").then(function(response) {
					$scope.page = response.data;
				}, function(response) {
					appService.notifications.queue({
						message: "The server is experiencing some problems at the moment. Sorry!",
						type: "error"
					})
				});
			}
		});

	};

	$scope.save = function() {
		page = {
			"page": $scope.page
		}

		if (page.id === '') {
			pageService.add(page).then(function(response) {
				$scope.page = response.data;
				appService.$location.url('/' + getUrl());
			}, function(response) {
				if (response.status == 500) {
					appService.notifications.queue({
						message: "The server is experiencing some problems at the moment. Sorry!",
						type: "error"
					});
				}
			});
		} else {
			pageService.update(page).then(function(response) {
				$scope.page = response.data;
				appService.$location.url('/' + getUrl());
			}, function(response) {
				if (response.status == 500) {
					appService.notifications.queue({
						message: "The server is experiencing some problems at the moment. Sorry!",
						type: "error"
					});
				}
			});
		}
	};
	appService.ready(init);
}]);
