{
  "targets": [
    {
      "target_name": "mysqrt",
      "sources": [ "mysqrt.cc" ],
      "libraries": [ "/usr/lib/libmymath.so" ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
