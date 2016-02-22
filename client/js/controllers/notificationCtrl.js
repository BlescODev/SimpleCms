app.controller('notificationCtrl', ['appService', '$scope', function(appService, $scope){

    $scope.current = {};

    var autoclose = function (notification) {
        if(notification.time){
            appService.$timeout(function () {
                $scope.close(notification);
            }, notification.time);
        }
    };

    appService.ready(function () {

        appService.notifications.registerObserver(function (notification) {
            if(notification){
                $scope.current = notification;
                $scope.visible = true;
                if($scope.current.time) {
                    autoclose(notification);
                }
            }
        });

    });

    $scope.close = function (notification) {
        if(!notification){
            notification = $scope.current;
        }

        if(angular.equals(notification, $scope.current)) {
            $scope.visible = false;
        }

        appService.$timeout(function () {
            if(notification.callback){
                if(typeof notification.callback === 'function'){
                    notification.callback();
                }
            }
            appService.notifications.close();
        }, 500);
    };


}]);
