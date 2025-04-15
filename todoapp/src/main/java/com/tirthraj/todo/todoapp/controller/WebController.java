package com.tirthraj.todo.todoapp.controller;


import com.tirthraj.todo.todoapp.model.Todo;
import com.tirthraj.todo.todoapp.repository.TodoRepository;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class WebController {

    private final TodoRepository todoRepository;

    public WebController(TodoRepository todoRepository) {
        this.todoRepository = todoRepository;
    }

    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("todos", todoRepository.findAll());
        return "index";
    }

    @PostMapping("/add")
    public String add(@RequestParam String task) {
        Todo todo = new Todo();
        todo.setTask(task);
        todo.setCompleted(false);
        todoRepository.save(todo);
        return "redirect:/";
    }

    @PostMapping("/toggle/{id}")
    public String toggle(@PathVariable Long id) {
        Todo todo = todoRepository.findById(id).orElseThrow();
        todo.setCompleted(!todo.isCompleted());
        todoRepository.save(todo);
        return "redirect:/";
    }

    @PostMapping("/delete/{id}")
    public String delete(@PathVariable Long id) {
        todoRepository.deleteById(id);
        return "redirect:/";
    }
}

