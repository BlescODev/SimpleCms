app.controller('notificationCtrl', ['appService', '$scope', function(appService, $scope){

    $scope.current = {};

    var autoclose = function () {
        if($scope.current.time){
            appService.$timeout(function () {
                $scope.close();
            }, $scope.current.time);
        }
    };

    appService.ready(function () {

        appService.notifications.registerObserver(function (notification) {
            if(!$scope.current.message){
                $scope.current = notification;
                $scope.visible = true;
                autoclose();
            }
        });

    });


    $scope.close = function () {
        $scope.visible = false;

        appService.$timeout(function () {
            if($scope.current.callback){
                if(typeof $scope.current.callback === 'function'){
                    $scope.current.callback();
                }
            }
            appService.notifications.close();
            $scope.current = appService.notifications.getNewest();
            autoclose();
            if($scope.current.message){
                $scope.visible = true;
            }
        }, 500);
    };


}]);
