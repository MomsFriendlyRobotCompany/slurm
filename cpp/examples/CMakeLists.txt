list(APPEND apps
    main
)

foreach(src ${apps})
    add_executable(${src} ${src}.cpp)
    target_link_libraries(${src} ${PROJECT_NAME})
endforeach()
