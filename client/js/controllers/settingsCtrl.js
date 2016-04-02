app.controller('settingsCtrl', ['appService', '$scope', '$routeParams', function(appService, $scope, $routeParams){
	$scope.setting = $routeParams.setting;
}]);
