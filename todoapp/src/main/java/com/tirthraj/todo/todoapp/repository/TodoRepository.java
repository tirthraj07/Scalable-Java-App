package com.tirthraj.todo.todoapp.repository;

import com.tirthraj.todo.todoapp.model.Todo;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TodoRepository extends JpaRepository<Todo, Long> {}
