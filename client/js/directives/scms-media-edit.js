app.directive('scmsMediaEdit', function($compile){
	return {
		restrict: 'E',
		scope: {
			media: "="
		},
		templateUrl: "/html/directives/scms-media-edit.tpl.html",

		link: function (scope) {
			scope.newMedia = {type:"", source:""};
			
			scope.addMedia = function () {
				var size = Object.keys(scope.media).length
				scope.media[size +1] = scope.newMedia;
				scope.newMedia = {type:"", source:""};
			};

			scope.removeMedia = function (index) {
				for(index = index+1; index < Object.keys(scope.media).length; index++) {
					scope.media[index] = scope.media[index+1]
				};
				delete scope.media[index];
			};
		}
	};
});
