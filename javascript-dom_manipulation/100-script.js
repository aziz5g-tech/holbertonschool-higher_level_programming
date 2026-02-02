document.addEventListener('DOMContentLoaded', function() {
  document.querySelector('#add_item').addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newItem);
  });

  document.querySelector('#remove_item').addEventListener('click', function() {
    const list = document.querySelector('.my_list');
    const items = list.querySelectorAll('li');
    if (items.length > 0) {
      list.removeChild(items[items.length - 1]);
    }
  });

  document.querySelector('#clear_list').addEventListener('click', function() {
    const list = document.querySelector('.my_list');
    list.innerHTML = '';
  });
});
