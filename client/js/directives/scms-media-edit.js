app.directive('scmsMediaEdit', function($compile){
	return {
		restrict: 'E',
		scope: {
			media: "="
		},
		templateUrl: "/html/directives/scms-media-edit.tpl.html",

		link: function (scope) {
			scope.newMedia = {type:"", source:""};
			
			scope.editMedia = function(index) {
				var mediaEdit = document.getElementById("media-edit-" + index);
				mediaEdit.style.display = "initial";
			}

			scope.updateMedia = function(index) {
				var mediaEdit = document.getElementById("media-edit-" + index);
				mediaEdit.style.display = "none";
			}

			scope.addMedia = function () {
				var mediaEdit = document.getElementById("media-edit");
				mediaEdit.style.display = "initial";
			};

			scope.cancelMedia = function () {
				var mediaEdit = document.getElementById("media-edit");
				mediaEdit.style.display = "none";
				scope.newMedia = {type:"", source:""};
			};

			scope.saveMedia = function () {
				var size = Object.keys(scope.media).length
				scope.media[size +1] = scope.newMedia;

				var mediaEdit = document.getElementById("media-edit");
				mediaEdit.style.display = "none";
	
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
