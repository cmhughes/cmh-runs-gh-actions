#!/bin/bash

function checkgitdiff
{
    git diff --quiet
    result=$? && [[ result -gt 0  ]] &&   echo "git diff has differences, something has changed" && exit
}


# comment here
echo "hello world, from cmh, more: helper thing next"
latexindent.pl -h
checkgitdiff
exit 0
