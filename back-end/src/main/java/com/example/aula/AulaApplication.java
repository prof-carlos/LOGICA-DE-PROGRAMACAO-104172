package com.example.aula;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.File;

@SpringBootApplication
public class AulaApplication {

	public static void main(String[] args) {
		io.github.cdimascio.dotenv.Dotenv dotenv = io.github.cdimascio.dotenv.Dotenv.configure()
			.directory(resolveBackendDirectory())
			.ignoreIfMalformed()
			.ignoreIfMissing()
			.load();

		dotenv.entries().forEach(entry -> {
			if (System.getenv(entry.getKey()) == null) {
				System.setProperty(entry.getKey(), entry.getValue());
			}
		});

		SpringApplication.run(AulaApplication.class, args);
	}

	private static String resolveBackendDirectory() {
		File currentDirectory = new File(System.getProperty("user.dir"));
		File backendDirectory = new File(currentDirectory, "back-end");
		return backendDirectory.isDirectory() ? backendDirectory.getPath() : currentDirectory.getPath();
	}

}
