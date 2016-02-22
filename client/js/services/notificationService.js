app.service('notificationService', [function ($q) {

    var notifications = [];

    var observers = [];

    var notifyObservers = function () {
        for(var i = 0; i < observers.length; i++) {
            observers[i](notifications[0]);
        }
    };

    return {
        registerObserver: function (callback) {
            if(typeof callback === 'function'){
                observers.push(callback);
            } else {
                console.error("Tried to register a non function as an observer of the notifications!");
            }
        },
        queue: function (notification) {
            if(notification.message) {
                var newMessage = true;
                for(var i = 0; i < notifications.length; i++){
                    if(JSON.stringify(notification) === JSON.stringify(notifications[i])) {
                        newMessage = false;
                        break;
                    }
                }
                if(newMessage) {
                    notifications.push(notification);
                    notifyObservers();
                }
            } else {
                console.error("A notification must contain a message!");
            }
        },
        close: function (notification) {
            notifications.splice(0, 1);
        },
        getNewest: function () {
            if(notifications.length > 0){
                return notifications[0];
            } else {
                return {};
            }
        }
    }

}]);
