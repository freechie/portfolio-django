import React from 'react';

export function capitalize(s) {
  if (typeof s !== 'string') return '';
  return s.charAt(0).toUpperCase() + s.slice(1);
}

export const LoadingAnimation = () => (
  <div className="flex justify-center items-center">
    <div className="animate-spin"></div>
  </div>
);
