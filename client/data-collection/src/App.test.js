import React from 'react';
import { render } from '@testing-library/react';
import Information from '../src/components/QuestionTypes/Information'
test('renders learn react link', () => {
  const { getByText } = render(<Information/>);
});
