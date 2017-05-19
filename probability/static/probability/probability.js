$(document).ready(function() {
   $('.click').attr('hidden', true);

   var probability = {

     'reset': function () {
       this.begin = undefined;
       this.events_data = [];
       this.event = true;
       this.last_event = undefined;
       this.true_count = 0;
       this.false_count = 0;
       this.true_sequence_max = 0;
       this.false_sequence_max = 0;
       this.sequence_max = 0;
       this.count = 0;
       this.false_probability = 0,
       this.true_probability = 0;
     },

     'date_now': function (date_now) {
       return date_now.toString().slice(-7,);
     },

     'sequence_max_calculation': function() {
       //console.log(Date.now(), Date.now().toString().slice(-7,))
       this.events_data.push([String(Date.now())[0], this.event])
       if (this.event===this.last_event || this.last_event===undefined) {
         this.sequence_max++;;
         if (this.last_event===undefined) {
           this.last_event = this.event;
         }
       } else {
         this.sequence_max = 1;
         this.last_event = this.event;
       }
       if (this.event) {
         var event_sequence_max = 'false_sequence_max';
       } else {
         var event_sequence_max = 'true_sequence_max';
       }
       if (this.sequence_max > this[event_sequence_max]) {
         this[event_sequence_max] = this.sequence_max;
       }
     },

     'timeId': function() {
       setInterval(function() {
         probability.event = !probability.event;
       }, 1);
     },
   };

   probability.reset();

   $('.run').on('click', function() {
     if (probability.experimenting) {
       probability.reset();
       $(this).text('Run');
       clearInterval(probability.timeId());
       $('.click').attr('hidden', true);
     } else {
       $(this).text('Stop');
       probability.timeId();
       $('.click').attr('hidden', false);
     }
     probability.experimenting = !probability.experimenting

   });

   $('.click').on('click', function() {
     if (!probability.experimenting) {
       return
     }
     probability.count++;
     if (probability.begin === undefined) {
       probability.begin = probability.date_now(Date.now())
     }
     var date_diff = probability.date_now(Date.now()) - probability.begin


     if (probability.event) {
       probability.true_count++;
       //probability.true_sequence_max;
     } else {
       probability.false_count++;
     }

     probability.sequence_max_calculation()

     probability.false_probability = probability.false_count / probability.count;
     probability.true_probability = probability.true_count / probability.count;
     console.log(probability.event, probability.count, date_diff, '\n',
       probability.true_count, probability.true_probability, '\n',
       probability.false_count, probability.false_probability, '\n',
       probability.true_sequence_max, probability.false_sequence_max, '\n',

     );
   });
});