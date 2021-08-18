function deleteTodo(todoId) {
   let path = "delete_todo/" + todoId + "/";
   location.replace(path);
}

function updateTodo(todoId) {
  let path = "update_todo/" + todoId + "/";
  location.replace(path);
}
