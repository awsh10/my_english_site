$(document).ready(function() {

  var englishWordObject = {
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
       $('#english-word').val(englishWordObject.englishWord);
       $('#transcription').val(englishWordObject.transcription),
       $('#russian-word').val(englishWordObject.russianWord);
    },
    'getDataFromServer': function(callback) {
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
          var msg = 'The word "' + englishWordObject.englishWord  + '" is not found.';
          alert(msg);
        } else {
           englishWordObject.englishWord = obj.english_word;
           englishWordObject.transcription = obj.transcription;
           englishWordObject.russianWord = obj.russian_word;
           englishWordObject.accessCount = obj.access_count;
           $('.not-find').attr('hidden', false);
           if (callback) {
             callback();
           };
        };
      });
    },
    'setDataToServer': function() {

    },
    'match_word': function() {
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
      }
      return return_value;
    },
  };

  englishWordObject.url = $('#server-data').attr('data-url');

  $('.exec').on('click', function() {
      englishWordObject.getDataFromPage();
      if ($('input[name=mode]:checked').val()==='find') {
        $('.not-find').attr('hidden', true);
        if (englishWordObject.match_word().match===false) {
          alert(englishWordObject.match_word().msg);
        } else {
          englishWordObject.getDataFromServer(englishWordObject.setDataToPage);
          englishWordObject.setDataToPage();
        }
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
                'englishWordObject': englishWordObject,
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