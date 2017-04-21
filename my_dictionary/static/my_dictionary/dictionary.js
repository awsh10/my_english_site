$(document).ready(function() {

    $('.exec').on('click', function() {
      function insertValue(transcription, russianWord, accessCount) {
          $('#russian-word').val(russianWord);
          $('#transcription').val(transcription);
          $('#access_count').val(accessCount);
        };

      var url = $('#server-data').attr('data-url')
      var englishWord = $('#english-word').val()

      if ($('input[name=mode]:checked').val()==='find') {
        insertValue('', '', '');

        if (englishWord.match(/[^a-z]/g) != null || englishWord === '') {
            msg = 'The expression "' + englishWord + '" is not a word!';
            alert(msg);
        } else {
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
      };

   });

   $('.mode').on('click', function() {
     if (this.value==='find') {
       $('.not-find').attr('hidden', true);
     } else {
       $('.not-find').attr('hidden', false);
     }
     ;
   });
});
