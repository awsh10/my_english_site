$(document).ready(function() {
  var englishWordObj = {
    'englishWord': '',
    'transcription': '',
    'russianWord': '',
    'url': '',
    'getDataFromPage': function () {
       this.englishWord = $('#english-word').val();
       this.transcription = $('#transcription').val(),
       this.russianWord = $('#russian-word').val();
    },
    'setDataToPage': function () {
       $('#english-word').val(englishWordObj.englishWord);
       $('#transcription').val(englishWordObj.transcription),
       $('#russian-word').val(englishWordObj.russianWord);
       $('access-count').val(englishWordObj.accessCount);
    },
    'getDataFromServer': function(function_object) {
      $.ajax({
        url: this.url + 'find',
        type: "GET",
        data:{
          'englishWord': this.englishWord,
        },
        dataType: 'text'
      }).done(function(data) {
        var obj = $.parseJSON(data);

        if (obj === false) {
          var msg = 'The word "' + englishWordObj.englishWord  + '" is not found.';
          englishWordObj.transcription = '';
          englishWordObj.russianWord = '';
          englishWordObj.accessCount = 0;
          alert(msg);
        } else {
           englishWordObj.englishWord = obj.english_word;
           englishWordObj.transcription = obj.transcription;
           englishWordObj.russianWord = obj.russian_word;
           englishWordObj.accessCount = obj.access_count;
           $('.not-find').attr('hidden', false);
        };

        if (function_object) {
          function_object();
        };
      });
    },
    'setDataToServer': function() {
      this.csrf();
      $.ajax({
          url: this.url + 'insert/',

          type: "POST",
          data: {
            'englishWord': englishWordObj.englishWord,
            'transcription': this.transcription,
            'russianWord': this.russianWord,
          },
          /*{
              'englishWordObj': englishWordObj,
          },*/
          dataType: 'text'
          })
            .done(function(data) {
              var obj = $.parseJSON(data);
              console.log(obj);
              alert(obj)
/*
              if (obj === false) {
                var msg = 'The word "' + englishWord + '" not is found.';
                $('.not-find').attr('hidden', true);
                alert(msg);
              }
*/
          });
    },
    'matchWord': function() {
      var return_value = {};
      if (this.englishWord.match(/[^a-z]/g) != null || this.englishWord === '') {
          msg = 'The expression "' + this.englishWord + '" is not a word!';
          this.russianWord = '';
          this.transcription = '';
          this.accessCount = 0;
          this.setDataToPage();
          return_value.msg = msg;
          return_value.match = false;
      } else {
        return_value.match = true;
      };
      return return_value;
    },
    'matchRussianWord': function() {console.log('matchRusianWord')
      var return_value = {};
      if (this.russianWord.match(/[^а-я]/g) != null || this.russianWord === '') {
          msg = 'The expression "' + this.russianWord + '" is not a word!';
          //this.russianWord = '';
          //this.transcription = '';
          //this.accessCount = 0;
          //this.setDataToPage();
          return_value.msg = msg;
          return_value.match = false;
      } else {
        return_value.match = true;
      };
      return return_value;
    },
    'csrf': function() {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = $.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                   }
               }
           }
            return cookieValue;
       }

        var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
       }
         $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
               }
           }
        });
     },
  };

  englishWordObj.url = $('#server-data').attr('data-url');

  $('.exec').on('click', function() {
      englishWordObj.getDataFromPage();
      if ($('input[name=mode]:checked').val()==='find') {
        $('.not-find').attr('hidden', true);
        if (englishWordObj.matchWord().match===false) {
          alert(englishWordObj.matchWord().msg);
        } else {
          englishWordObj.getDataFromServer(englishWordObj.setDataToPage);
        };
      } else if ($('input[name=mode]:checked').val()==='insert') {
        if (englishWordObj.matchWord().match===false) {
          alert(englishWordObj.matchWord().msg);
        } else if (englishWordObj.matchRussianWord().match===false) {alert(11111)
          alert(englishWordObj.matchRussianWord().msg);
        } else {
          englishWordObj.setDataToServer();
        };
      };


   });

   $('.mode').on('click', function() {
     if (this.value==='find') {
       $('.not-find').attr('hidden', true);
     } else {
       $('.not-find').attr('hidden', false);
     };
   });


});

/*




          }
            $.ajax({
                url: url + englishWord,
                type: "GET"
            //data:{
            //    'englishWord': englishWord,
           //},
            //dataType: 'text'
           })
            .done(function(data) {
                var obj = $.parseJSON(data);

                if (obj === false) {
                  var msg = 'The word "' + englishWord + '" not is found.';
                  $('.not-find').attr('hidden', true);
                  alert(msg);
                 } else if (obj === englishWord) {
                     $('.not-find').attr('hidden', true);
                     insertValue('', '', '')
                     msg = 'The path "' + englishWord + '" is not a word'
                     alert(msg)
                 } else {
                     insertValue(obj.transcription, obj.russian_word, obj.access_count)
                     $('.not-find').attr('hidden', false);
                 }
            });
        }
      } else if ($('input[name=mode]:checked').val()==='insert') {
          $.ajax({
            url: url + 'insert',
            type: "POST"
            data:{
                'englishWordObj': englishWordObj,
            },
              dataType: 'text'
           })
            .done(function(data) {
               var obj = $.parseJSON(data);

                if (obj === false) {
                  var msg = 'The word "' + englishWord + '" not is found.';
                  $('.not-find').attr('hidden', true);
                  alert(msg);

      };

   });

});
*/