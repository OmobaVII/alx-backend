const kue = require('kue');
const queue = kue.createQueue();

const jobObject = {
  phoneNumber: '08100042858',
  message: 'Hello from Employee',
};

const job = queue.create('push_notification_code', jobObject);

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.save((error) => {
  if(!error) {
    console.log(`Notification job created: ${job.id}`);
  } else {
    console.error('Error creating job:', error);
  }
});
